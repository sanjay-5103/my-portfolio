// Reveal on scroll
function revealOnScroll() {
    const els = document.querySelectorAll('.fade-up');
    const threshold = window.innerHeight - 60;
    els.forEach(el => {
        const rect = el.getBoundingClientRect();
        if (rect.top < threshold) el.classList.add('visible');
    });
}
document.addEventListener('scroll', revealOnScroll);
document.addEventListener('DOMContentLoaded', revealOnScroll);

// 3D tilt on hover
document.querySelectorAll('[data-tilt]').forEach(card => {
    let rect;
    const max = 15;
    function setRect(){ rect = card.getBoundingClientRect(); }
    setRect(); window.addEventListener('resize', setRect);
    card.addEventListener('mousemove', (e) => {
        const x = e.clientX - rect.left;
        const y = e.clientY - rect.top;
        const rx = ((y / rect.height) - 0.5) * -2 * max;
        const ry = ((x / rect.width) - 0.5) * 2 * max;
        card.style.transform = `rotateX(${rx}deg) rotateY(${ry}deg) translateY(-4px)`;
    });
    card.addEventListener('mouseleave', () => {
        card.style.transform = '';
    });
});

