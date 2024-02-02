# Unit Testing
Unit testing is applied on every individual unit of a software product. In python, there is a built in library called `unittest` for unit testing.
## Benefits
- Early Bug Detection
- Code Maintainability
- Regression Testing
- Facilitates Collaboration
## Steps
1. First we need to write down the class with its functionalities. Here I've written a `customer.py` file with four functionalities of a Customer class:
   - return Fullname
   - return Email
   - Raise pay amount by 5%
   - Check Monthly Schedule URL (imported 'requests' library for this) 
   
<img src="https://github.com/jannat-349/Unit-test-practice-in-python/assets/50805240/6a12b342-143d-4794-bf53-bf6e87c165bf" alt="image" height="400"/>

2. Then create a `test_customer.py` an import the necessary libraries.

<img src="https://github.com/jannat-349/Unit-test-practice-in-python/assets/50805240/10cc5db7-5617-42b6-b9de-1fdf5b28a15f" alt="image" height="100"/>

3. Inside the `TestCustomer` class, write down a `setUpClass` that will run before everything. We can use this to define global variables or databases. Also a `tearDownClass` that will run after everything. We can delete the global variables or databases here.
4. Write down a `setUp` function that will run before every test case. We can declare common functionalities like customer creation here. Similarly, a `tearDown` function for deletion.

<img src="https://github.com/jannat-349/Unit-test-practice-in-python/assets/50805240/607f8995-438d-4ffd-a53d-491bfb4c3fc5" alt="image" height="400"/>


5. Write down the test cases as functions. The test case functions should be named like `test_email()`, `test_fullname()`, etc.
6. Inside the testcases check validity on any type of changes using built in `asserEqual` function of unittest library.

| ![image](https://github.com/jannat-349/Unit-test-practice-in-python/assets/50805240/036566f2-1a7c-4b2b-beb8-87025ce7d878) | ![image](https://github.com/jannat-349/Unit-test-practice-in-python/assets/50805240/292e5a36-1e6d-4660-8a97-387bce15a5ae) | 
|--|--|
| ![image](https://github.com/jannat-349/Unit-test-practice-in-python/assets/50805240/b3ee5c25-d50c-4f37-a760-0395e8d16c79) | ![image](https://github.com/jannat-349/Unit-test-practice-in-python/assets/50805240/7acba5cf-28d0-422a-9ae5-6800ff1fe83a) |

7. To run the test cases without calling add this in the end.

![image](https://github.com/jannat-349/Unit-test-practice-in-python/assets/50805240/db60e589-985b-4c92-bfb6-777565e751ea)

8. Now run the file. It will show OK if there is no error(like below). Otherwise it will show error.

<img src="https://github.com/jannat-349/Unit-test-practice-in-python/assets/50805240/d60dd9dc-30f6-4095-a329-5ce0ef515e25" alt="image" height="400"/>

## Video Link
[Click Here](https://youtu.be/6tNS--WetLI?si=KQ3RxWsW7jeBPvSW)






