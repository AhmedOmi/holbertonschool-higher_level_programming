#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - check of a list
 * @list: pointer of list
 * Return: return int
 */
int check_cycle(listint_t *list)
{
listint_t *x = list, *a = list;
while (a && a->next)
{
x = x->next;
a = a->next->next;
if (x == a)
return (1);
}
return (0);
}
