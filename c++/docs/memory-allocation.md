

# Difference between dynamic and static memory allocation.

In C++ we can typically allocate memory locations for variables and objects either during the compile time or during runtime.
As per the names suggest, static memory location is the process of allocating memory locations during the compile time.
While, dynamic memory allocation is the process of allocating memory addresses during the runtime.

Another difference between these two is that in C++, a statically allocated memory location is automatically de-allocated once the object is out of scope. For example, if you define a variable inside a function, the memory allocated for that variable is automatically de-allocated once the function has finished executing.

Meanwhile for any dynamically allocated memory locations, we need to explicitly de-allocate the memory locations using the delete() function in C++.

Dynamic memory allocation can be achieved in C++ using the new Keyword while defining an object. While just simply calling the constructor function would allow us to statically allocate a memory location.

```
void static_allocation(){
    // statically allocate the integer value 1 in variable x.
    int x = 1;
    
    // print the value in x.
    cout << x << endl;
}

void dynamic_allocation(){
    // dynamically allocate a memory address for an integer and store that address in a pointer variable px.
    int * px = new x(5);

    // print the value of integer in the pointer variable px.
    cout << *px << endl; 

    // de-allocate memory location for the pointer variable px.
    delete(px); 
}
```

Additionally, it is also notable that using the new keyword returns the memory address of the newly created object while simply calling the constructor function on a class returns the object itself.

```
int(5); // returns an integer value 5.

new int(5); // returns the memory address of the created integer value 5.
```