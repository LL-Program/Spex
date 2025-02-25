# Spe* General C++ Coding Guidelines - Lukas Rennhofer @2025

## 1. Code Readability
### 1.1. Naming Conventions

Classes and Structures: Use **PascalCase** (e.g., ```NPCComponent```, ```EntityManager```).
Functions and Methods: Use **camelCase** (e.g., ```generateNPC()```, ```calculateHealth()```).
Variables: Use camelCase for **local variables** and **function parameters** (e.g., ```currentPosition```, ```npcList```).
Constants: Use ```UPPER_SNAKE_CASE``` (e.g., ```MAX_LEVEL```, ```MAX_SPEED```).
Enumerations: Use **PascalCase** for enumeration types and values (e.g., ```class NPCType { SOLDIER, TRADER };```).

### 1.2. Descriptive Names

Choose names for variables, functions, and classes that clearly represent their purpose.
**Avoid** single-character variable names (e.g., use ```npcList``` instead of ```n```).
Function names should describe the action they perform (e.g., ```loadWorldData()``` instead of ```read()```).

### 1.3. Commenting

Comments should explain why something is being done, not what is being done (the code itself should be clear about what it does).
Comment on complex logic or algorithms in functions.
Every function should have a header comment, especially for public APIs and critical sections.


```
/**
 * Calculates the movement vector based on the current position and velocity of the entity.
 *
 * @param position The current position of the entity.
 * @param velocity The velocity vector influencing the entity's movement.
 * @return A new position after applying the movement.
 */
Vector3 calculateMovement(Vector3 position, Vector3 velocity);
```
### 1.4. Avoiding Complexity

Avoid really deep nesting of loops and conditionals if its possible. If nesting exceeds **5 levels**, refactor the code if needed.
Use Guard Clauses to minimize nested conditions.

```
// Instead of:
if (condition) {
    if (anotherCondition) {
        // do something
    }
}

// Use Guard Clauses:
if (!condition) return;
if (!anotherCondition) return;
// do something
```
## 2. Code Structure
### 2.1. Brackets and Block Formatting

Always use curly braces ```{}``` for all control structures (even if the block contains only one statement).
The opening curly brace should be placed on the same line as the control structure (**K&R style**).
The closing curly brace should align vertically with the beginning of the statement (at the same indentation level).

```
if (someCondition) {
    doSomething();
} else {
    doSomethingElse();
}
```

### 2.2. Indentation and Spacing

Use **4 space**s per indentation level (avoid tabs).
Add one blank line between function definitions for clarity.
Avoid trailing spaces at the end of lines.
**Align code** for readability, especially for long function arguments or assignments.

```
void generateNPC(uint32_t entityID, 
                 EntityManager& entityManager, 
                 ComponentManager& componentManager) {
    // Code here
}
```

### 2.3. Line Length

Limit lines to **80-100** characters.
Break long lines into multiple lines to keep the code readable.

### 2.4. Functions and Methods

Each function should perform **one task only** (Single Responsibility Principle). If the function becomes too large or complex, break it down into smaller helper functions.
Prefer **short functions** (max 30 lines), as they are easier to understand and test.

## 3. Classes and Object-Oriented Principles
### 3.1. Class Definitions

Private Members: Keep class members **private** and provide **public getter/setter methods** when necessary.
Constructors and Destructors: Define and implement destructors if dynamic memory allocation is used. If not needed, delete or avoid the constructor.

```
class NPC {
private:
    std::string name;
    int health;

public:
    NPC(const std::string& npcName, int npcHealth)
        : name(npcName), health(npcHealth) {}

    // Getter and Setter Methods
    std::string getName() const { return name; }
    void setHealth(int health) { this->health = health; }
};
```

### 3.2. Constructor Initialization List

Always use the constructor initialization list to initialize class members.
Avoid assigning values within the constructor body unless they depend on logic (e.g., if default values depend on logic).

```
class Entity {
private:
    int x, y;

public:
    Entity(int xPos, int yPos) : x(xPos), y(yPos) {}
};
```

### 3.3. Polymorphism

Use **virtual functions** to enable polymorphism. Override virtual functions when extending a class.
Implement virtual destructors in base classes if inheritance is used.

```
class Entity {
public:
    virtual void update() = 0; // Pure virtual function
    virtual ~Entity() = default; // Virtual Destructor
};

class NPC : public Entity {
public:
    void update() override {
        // NPC-specific logic
    }
};
```

## 4. Error Handling
### 4.1. Best Practices for Error Handling

Use exceptions to report errors, and ensure the system fails safely.
Catch exceptions only where necessary to handle them, and avoid catching exceptions globally unless it is for logging or rethrowing.

```
try {
    // Risky operation
    processFile();
} catch (const std::exception& e) {
    Logger::logError("Error processing the file: " + std::string(e.what()));
    throw;  // Rethrow the exception
}
```

### 4.2. Assertions

Use assertions to check assumptions during development and debugging.
Ensure assertions do not impact production performance. They should be used to detect programming errors.

```
assert(entity != nullptr);  // Ensure the entity is not null
```

## 5. Memory Management
### 5.1. Use RAII (Resource Acquisition Is Initialization)

Always use **RAII** for managing resources like memory, file handles, and network sockets (e.g., ```std::unique_ptr```, ```std::shared_ptr```).
Avoid manual memory management unless absolutely necessary. Prefer standard containers over raw pointers.

```
std::unique_ptr<Entity> entity = std::make_unique<Entity>(position);
```

### 5.2. Avoiding Memory Leaks

When manual memory management is necessary (e.g., in special low-level tasks), use **smart pointers** to handle memory correctly.

## 6. Testing and Debugging
### 6.1. Unit Testing

Write **unit tests** for every really big function, method or module.
Tests should be easy to run and cover both **normal and edge cases**.

```
void TEST_qLhSD(EntityTests, TestMoveEntity) {
    Entity entity(0, 0);
    entity.move(5, 5);
    ASSERT_EQ(entity.getX(), 5);
    ASSERT_EQ(entity.getY(), 5);
}
```

### 6.2. Debugging

Ensure **debug logs** are available to help diagnose issues, but avoid excessive logging in production.
Use conditional logging to limit excessive log outputs in production.

## 7. Version Control and Collaboration
### 7.1. Git Best Practices

**Commit regularly** with **meaningful messages** that explain what has changed and why.
Follow a branching strategy (e.g., feature branches, develop/master branches).
Ensure code reviews are conducted, and verify that all guidelines are followed before merging code.

## Conclusion

These guidelines are designed to ensure that the code remains **clear, maintainable, and reliable**, inspired by best practices from various industries. The focus is on code clarity, error prevention, modularity, and robust testing.

---

### Written By Lukas Rennhofer @2025 | V.1.0.0