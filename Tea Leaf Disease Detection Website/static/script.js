const canvas = document.getElementById('canvas');
const ctx = canvas.getContext('2d');

let leaves = [];

canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

class Leaf {
    constructor() {
        this.image = new Image();
        this.image.src = 'static/leaf.png'; // Make sure you have an image named 'leaf.png' in the same directory
        this.x = Math.random() * canvas.width;
        this.y = -50;
        this.speed = Math.random() * 2 + 1;
    }

    fall() {
        this.y += this.speed;
        if (this.y > canvas.height) {
            this.y = -50;
            this.x = Math.random() * canvas.width;
        }
    }

    draw() {
        ctx.drawImage(this.image, this.x, this.y, 200, 150); // Adjust size as needed
    }
}

function animate() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    leaves.forEach(leaf => {
        leaf.fall();
        leaf.draw();
    });

    requestAnimationFrame(animate);
}

for (let i = 0; i < 20; i++) {
    leaves.push(new Leaf());
}

animate();

