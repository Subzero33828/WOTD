// sSpringbootnotes.java 
// This file contains a simple Spring Boot application with REST endpoints
// It demonstrates how to create a basic web service that responds to HTTP GET requests
/* 08/12/2025 
import org.springframework.boot.SpringApplicaion;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.*;

@SpringBootApplication
@RestController
public class DemoApplication {
    @GetMapping("/Hello")
    public String hello() {
        return "Hello, World!";}
    
        @GetMapping("/Greet/{name}")
        public String greet(@PathVariables String name)
        String name = Tyler
         {return "Hello, " + name + "!";}

    public static void main(String[] args) {
        SpringApplication.run(DemoApplication.class, args);
        }
}*/
// Package declaration - matches your folder structure
// Import necessary Spring Boot and Web annotations/classes
// Marks this class as a Spring Boot application
// Marks this class as a REST controller, allowing it to handle HTTP requests



package com.example.demo;

// Import necessary Spring Boot and Web annotations/classes
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.*;

// Marks this class as a Spring Boot application
@SpringBootApplication
public class NotesApplication { 
    public static void main(String[] args) {
        SpringApplication.run(NotesApplication.class, args);
    } 
}
// Marks this class as a REST controller, allowing it to handle HTTP requests
@RestController
public class DemoApplication {

    // =========================
    // Route 1: Simple Greeting
    // =========================
    // Maps HTTP GET requests to "/hello"
    // When you visit http://localhost:8080/hello, this method runs
    @GetMapping("/hello")
    public String hello() {
        return "Hello, World!"; // Returns a simple greeting
    }

    // =========================
    // Route 2: Greeting by Name
    // =========================
    // Maps GET requests to "/greet/{name}"
    // {name} is a "path variable" in the URL
    // Example: http://localhost:8080/greet/Tyler
    @GetMapping("/greet/{name}")
    public String greet(@PathVariable String name) {
        // The {name} part of the URL is automatically passed into this method
        return "Hello, " + name + "!"; // Returns personalized greeting
    }

    // =========================
    // Optional: Default Greeting
    // =========================
    // This version uses a query parameter instead of a path variable
    // Example: http://localhost:8080/greet?name=Tyler
    @GetMapping("/greet")
    public String greetQuery(@RequestParam(defaultValue = "Friend") String name) {
        // If no name is provided, it defaults to "Friend"
        return "Hello, " + name + "!";
    }

    // =========================
    // Main Method
    // =========================
    // Entry point for the Spring Boot application
    // Runs the embedded web server (Tomcat by default)
    public static void main(String[] args) {
        SpringApplication.run(DemoApplication.class, args);
    }
}
