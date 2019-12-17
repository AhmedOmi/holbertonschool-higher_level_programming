#include <stdio.h>
#include "lists.h"
/**
 * ip_helper - check function
 * @f: pointer to pointe list
 * @b: pointer list
 * @m: int pointer
 * Return: int
 */
int ip_helper(listint_t **f, listint_t *b, int *m)
{
if (b->next)
{
if (!ip_helper(f, b->next, m))
return (0);
if (*m)
return (1);
}
if ((*f)->n == b->n)
{
if (*f == b || (*f)->next == b)
*m = 1;
else
*f = (*f)->next;
return (1);
}
return (0);
}

/**
 * is_palindrome - function to verify palindrome linked list
 * @h: pointer of pointer head linked list
 * Return: int.
 */
int is_palindrome(listint_t **h)
{
listint_t **f = h;
int m = 0;
int a;
if (!h)
return (0);
if (!*h || !(*h)->next)
return (1);
a = ip_helper(f, (*h)->next, &m);
return (a);
}
