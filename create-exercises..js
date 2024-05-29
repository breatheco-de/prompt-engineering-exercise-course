const fs = require('fs');
const path = require('path');

const exercises = [
    "00- Brieftly understand Generative AI",
    "01 - What is Prompting",
    "02- Write your first prompt ",
    "02.1 - Importance of detailed instructions",
    "02.2 - Improve your first prompt ",
    "02.3 - Write detailed instruction for kids story ",
    "03 - Acting as an expert",
    "03.1 - Get more relevant information",
    "03.2 - Create Cooking Youtuber script",
    "04 - Delimiters and how to avoid missunderstanding",
    "04.1 - Fix the failing translation prompt",
    "05 - Let the model think",
    "05.1 - Improve accuracy in physics prompt",
    "06 - Some shots prompts",
    "06.1 - Obtaining a correct list of products",
    "07 - What is context in prompting",
    "07.1 - Become a superhero"
];

const slugify = (text) => {
    return text.toLowerCase()
        .replace(/[^\w\s.-]/g, '')  // Allow dots
        .replace(/\s+/g, '-')       // Replace spaces with hyphens
        .replace(/-+/g, '-');       // Replace multiple hyphens with a single hyphen
};

const rootDir = path.join(__dirname, 'exercises');

if (!fs.existsSync(rootDir)) {
    fs.mkdirSync(rootDir);
}

exercises.forEach(exercise => {
    const exerciseDir = path.join(rootDir, slugify(exercise));

    if (!fs.existsSync(exerciseDir)) {
        fs.mkdirSync(exerciseDir);
    }

    const readmeEnPath = path.join(exerciseDir, 'README.md');
    const readmeEsPath = path.join(exerciseDir, 'README.es.md');

    fs.writeFileSync(readmeEnPath, `# ${exercise}\n\n`);
    fs.writeFileSync(readmeEsPath, `# ${exercise} (ES)\n\n`);
});

console.log('Directories and README files created successfully.');
