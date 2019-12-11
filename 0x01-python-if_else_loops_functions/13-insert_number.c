#include "lists.h"
/**
 * insert_node - inserts a node into a sorted link list
 * @head: listint_t pointer
 * @number: integer
 * Return: returns list
 */
listint_t *insert_node(listint_t **head, int number)
{
listint_t *new = NULL
listint_s *prev = NULL;
new = malloc(sizeof(listint_t));
if (new)
{
new->n = number;
new->next = *head;
if (!new->next || new->n <= (*head)->n)
*head = new;
else
while (new->next && new->n > new->next->n)
{
prev = new->next;
new->next = prev->next;
}
if (prev)
prev->next = new;
}
return (new);
}
