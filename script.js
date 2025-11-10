const student = {
    name: "John Doe",
    age: 21,
    courses: ["Math", "Science", "History"],
    isActive: true,

    greet: function() {
        console.log(`Hello, my name is ${this.name}.`);
    }
}

student.greet();
student.name;


if (student.isActive) {
    console.log(`${student.name} is an active student.`);
} else if (!student.isActive) {
    console.log(`${student.name} is not an active student.`);
} else {
    console.log(`Status of ${student.name} is unknown.`);
}