## TypeScript
 
Typescript is a superset of JavaScript which adds types and additonal function to plane JavaScript. TypeScript can't be displayed by the browser. It needs a specific compiler to translate TypeScript into JavaScript. 

## Table of Contents 

- [TypeScript](#typescript)
- [Table of Contents](#table-of-contents)
- [Installation](#installation)
- [TypeScript Types](#typescript-types)
  - [Primitive Types](#primitive-types)
  - [Complex Types](#complex-types)
- [Type Inference](#type-inference)
  - [Union Type](#union-type)
  - [Creating own Types](#creating-own-types)
- [Functions \& Types](#functions--types)
  - [Special Return Value](#special-return-value)
- [Generics](#generics)
- [Classes](#classes)
- [Interfaces](#interfaces)


## Installation 

To install TypeScript first it's important to initalize a package .json where Typescript is been listet. To initalize this Json enter the following command:

```
npm init -y
```

This Command creates a empty package.json file.

After that we need to install TypeScript specific for this project. Therefore we need to enter the following command:

```
npm install typescript --save-dev
```

this command installs TypeScript specific for this project and also adds it to the package.json file. 

To compile a TypeScript file we need to run a specific command:
```
npx tsc with-typescript.ts
```

This Method is used to compile a specific file. 

**Auto Compile**
To auto compile all TypeScript files we have to enter the following command:
```
tsc --watch
```
to only auto compile one file enter the following command: 
```
tsc --watch myfile.ts
```


## TypeScript Types
The key feature in TypeScript is to add types to variables. There is a specific type list which is been listet here. 


### Primitive Types

```ts
// Int
let age: number;
age = 12.1 

//Str
let userName: string
userName= 'Max'

//Boolean
let isInstructor: boolean
isInstructor = true
```

### Complex Types

```ts
//Arrays
let hobbies: string[]
hobbies = ['Sport', 'Cooking']

//Objects
let person: {
    name: string,
    age: number
}
person={
    name: 'Max',
    age:32

}
//Example Combination
let combined: {
    people: string[], 
    age: number[]

}[] //this would be a list ob objects which contains string arrays and number arrays
```


## Type Inference 

Instead of declaring every datatype manuel in TypeScript it is recommended to use the Type Inference. This means that TypeScript is detecting automatically the datatype of the variable. This method should be used as much as possible. 

```ts
let course = 'React - The complete guide'
```

### Union Type

It is also possible to only allow specific Types for a specific variable.

```ts
let course: string | number = 'React - The complete guide
```

### Creating own Types

In TypeScript it is also possible to create youre own type which implifies youre own Type. This allows more easier code maintaining.

```ts
type Person = {
    name: string;
    age: number;
}
```

## Functions & Types 

by hovering over a function the input types of the function are displayed and also the return value type. It is also possible to specificly declare the return type. But if there is no reason for that, don't do that.

```ts
function add(a: number, b: number): number{
    return a+b
}
```

### Special Return Value 

```ts
function printOutput(value: any){
    console.log(value)
}
```

This return type in this function is void because this function will never return a value. 

## Generics 

**Current Problem:**
```ts
function insertAtBeginning(array: any[], value: any){
    const newArray= [value,...array] // copies the existing array
    return newArray
}

const demoArray =[1,2,3]
const updatedArray = insertAtBeginnin(demoArray,-1) // Output:[-1,1,2,3]
```
This return value will be the type any bcause if we want to use for example numbers or string we are unable to do so. 

**Solution:**
```ts
function insertAtBeginning <T>(array: T[], value: T){//diffrent
    const newArray= [value,...array] // copies the existing array
    return newArray
}

const demoArray =[1,2,3]
const updatedArray = insertAtBeginnin(demoArray,-1) // Output:[-1,1,2,3]
```

By defining the input as T we are able to look at the value types inside the value to identify the type of the arguement. 

## Classes 

We can describe all propertys and types of a class in advance before the constructor to create a blueprint with variables and methods. It is also possible to create private and public methods which can be accessed only inside the class or also from outside. 

```ts
class Student{
    firstName: string
    lastName:string
    age:number
    private courses: string[] //private variable not accessable from outside

    constructor(first: string, last: string, age: number, courses: string[]){
        this.firstName  = first
        this.lastName   = last
        this.age        = age
        this.courses    = courses
    }
    enrol(courseName: string){
        this.courses.push(courseName)
    }
    listCourses(){
        return this.courses.slice() 
    }
}

const student = new Student('Max', 'Woelfel', 32, ['angular','react'])
student.enrol('Vue')
console.log(student.courses) //Output: Angular, React, Vue


student.listCourses() //allows to enter the private variable
```

## Interfaces

Interfaces are implemented by classes which means, that the class is been described through the interface. Like as a blueprint for a class. 

```ts
interface Human{
    firstName: string
    age: number

    greet() => void
}


class Instructor implements Human{ //This class uses the Human interface
    firstName: string
    age: number
    greet(){
        console.log("Hello")
    }
}


//Other example
let max: Human
max={
    firstName: "Max"
    age: 25,
    greet(){
        console.log("Hello World!")
    }
}
```

