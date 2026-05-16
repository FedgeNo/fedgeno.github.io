import * as THREE from 'three';

function makeOrb(canvas) {
    const renderer = new THREE.WebGLRenderer({ canvas, alpha: true, antialias: true, powerPreference: 'high-performance' });
    const size = canvas.parentElement.clientWidth;
    renderer.setSize(size, size);
    renderer.setPixelRatio(Math.min(window.devicePixelRatio, 1.5));
    renderer.setClearColor(0x000000, 0);

    const scene  = new THREE.Scene();
    const camera = new THREE.PerspectiveCamera(45, 1, 0.1, 100);
    let camAngle = 0;

    const N    = 10000;
    const dirs = new Float32Array(N * 3);
    const Y    = new Float32Array(N * 7);
    const s32  = 1.22474487139, s152 = 1.9364916731,
          s15  = 3.87298334621, s58  = 0.79056941504;

    for (let i = 0; i < N; i++) {
        const t  = Math.acos(1 - 2 * Math.random());
        const p  = 2 * Math.PI * Math.random();
        const s  = Math.sin(t);
        const ux = s * Math.cos(p), uy = s * Math.sin(p), uz = Math.cos(t);
        dirs[i*3] = ux; dirs[i*3+1] = uy; dirs[i*3+2] = uz;
        const j = i * 7;
        Y[j]   = uz * (5*uz*uz - 3) * 0.5;
        Y[j+1] = ux * (5*uz*uz - 1) * s32;
        Y[j+2] = uy * (5*uz*uz - 1) * s32;
        Y[j+3] = uz * (ux*ux - uy*uy) * s152;
        Y[j+4] = ux * uy * uz * s15;
        Y[j+5] = ux * (ux*ux - 3*uy*uy) * s58;
        Y[j+6] = uy * (3*ux*ux - uy*uy) * s58;
    }

    const geo = new THREE.BufferGeometry();
    geo.setAttribute('position', new THREE.BufferAttribute(new Float32Array(N * 3), 3));
    geo.setAttribute('color',    new THREE.BufferAttribute(new Float32Array(N * 3), 3));
    const mat = new THREE.PointsMaterial({
        size: 0.11, vertexColors: true, transparent: true,
        opacity: 0.82, blending: THREE.AdditiveBlending, depthWrite: false
    });
    scene.add(new THREE.Points(geo, mat));

    const col  = new THREE.Color();
    const pos  = geo.attributes.position.array;
    const cols = geo.attributes.color.array;

    return function tick(t) {
        const w = t * 0.0006;
        let a0 = Math.cos(w),
            a1 = Math.sin(w) * Math.cos(w * 1.7) * 0.7,
            a2 = Math.sin(w) * Math.sin(w * 1.7) * 0.7,
            a3 = Math.sin(w) * Math.cos(w * 0.9) * 0.5,
            a4 = Math.sin(w) * Math.sin(w * 0.9) * 0.5,
            a5 = Math.sin(w) * Math.cos(w * 1.3) * 0.4,
            a6 = Math.sin(w) * Math.sin(w * 1.3) * 0.4;
        const n = Math.hypot(a0, a1, a2, a3, a4, a5, a6) || 1;
        a0/=n; a1/=n; a2/=n; a3/=n; a4/=n; a5/=n; a6/=n;

        for (let i = 0; i < N; i++) {
            const j  = i * 3, k = i * 7;
            const ux = dirs[j], uy = dirs[j+1], uz = dirs[j+2];
            const psi = a0*Y[k] + a1*Y[k+1] + a2*Y[k+2] + a3*Y[k+3]
                      + a4*Y[k+4] + a5*Y[k+5] + a6*Y[k+6];
            const d = psi * psi;
            if (d < 0.02) {
                pos[j] = pos[j+1] = pos[j+2] = cols[j] = cols[j+1] = cols[j+2] = 0;
                continue;
            }
            const r = 2.2 + 2.8 * Math.pow(d, 0.6);
            pos[j] = ux*r; pos[j+1] = uy*r; pos[j+2] = uz*r;
            col.setHSL(psi > 0 ? 0.58 : 0.06, 1.0, 0.55 + 0.25 * Math.pow(d, 0.2));
            cols[j] = col.r; cols[j+1] = col.g; cols[j+2] = col.b;
        }

        geo.attributes.position.needsUpdate = true;
        geo.attributes.color.needsUpdate    = true;
        camAngle += 0.008;
        camera.position.x = Math.cos(camAngle) * 22;
        camera.position.z = Math.sin(camAngle) * 22;
        camera.lookAt(0, 0, 0);
        renderer.render(scene, camera);
    };
}

const orbL = document.getElementById('orbL');
const orbR = document.getElementById('orbR');

if (orbL && orbR) {
    const left  = makeOrb(orbL);
    const right = makeOrb(orbR);
    (function animate(t) { requestAnimationFrame(animate); left(t); right(t); })(0);
    window.addEventListener('resize', () => {
        document.querySelectorAll('.corner-orb canvas').forEach(c => {
            const s = c.parentElement.clientWidth;
            c.width = s; c.height = s;
        });
    });
}
