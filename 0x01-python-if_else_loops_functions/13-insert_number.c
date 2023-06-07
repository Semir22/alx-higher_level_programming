#include "lists.h"

listint_t *insert_node(listint_t **head, int number)
{
	int checker = -1, i;
	listint_t *new;
	listint_t *current;
	listint_t *check;

	current = *head;
	check = *head;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;

	while (check->n < number)
	{
		checker++;
		check = check->next;
	}
	new->next = check;

	if (*head == NULL)
		*head = new;
	else
	{
		for (i = 0; i < checker; i++)
			current = current->next;
		current->next = new;
		while (current->next != NULL)
			current = current->next;
	}

	return (new);
}