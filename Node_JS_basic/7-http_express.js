const express = require('express');
const fs = require('fs');

const app = express();
const port = 1245;
const DB_FILE = process.argv[2];

/**
 * Logique de lecture adaptée pour retourner une chaîne de caractères
 */
function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
        return;
      }

      const lines = data.split('\n').filter((line) => line.trim() !== '');
      if (lines.length <= 1) {
        resolve('Number of students: 0');
        return;
      }

      const students = lines.slice(1);
      let output = `Number of students: ${students.length}`;

      const fields = {};
      for (const student of students) {
        const studentData = student.split(',');
        if (studentData.length >= 4) {
          const firstName = studentData[0];
          const field = studentData[3].trim();
          if (!fields[field]) fields[field] = [];
          fields[field].push(firstName);
        }
      }

      for (const [field, list] of Object.entries(fields)) {
        output += `\nNumber of students in ${field}: ${list.length}. List: ${list.join(', ')}`;
      }
      resolve(output);
    });
  });
}

// Route racine
app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

// Route /students
app.get('/students', async (req, res) => {
  const title = 'This is the list of our students\n';
  try {
    const data = await countStudents(DB_FILE);
    res.send(`${title}${data}`);
  } catch (error) {
    res.send(`${title}${error.message}`);
  }
});

app.listen(port);

module.exports = app;
