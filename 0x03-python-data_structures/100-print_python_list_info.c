#include <stdio.h>
#include <python.h>

/**
 * print_python_list_info - This is a function that print the python info
 * @p: pointer
 * Return: nothing
 */

void print_python_list_info(PyObject *p)
{
long int len, k;
pyListObject *list;
PyObject *item;

len = py_SIZE(p);
printf("[*] Size of the Python List = %ld\n", size);

list = (PyListObject *)p;
printf("[*] Alocated = %ld\n", list->allocated);

for (k = 0; k < len; k++)
{
iten = PyList_GetItem(p, k);
printf("Element %ld: %s\n", k, Py_TYPE(item)->tp_name);
}
}
