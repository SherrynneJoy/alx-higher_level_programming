#include "lists.h"

/**
 * check_cycle - checks if the linked list has a cycle
 * @list: pointer
 * Return: 0 when successful
 */
int check_cycle(listint_t *list)
{
	listint_t *hurry = list;
	listint_t *slowly = list;

	if (!list)
		return (0);
	while (slowly && hurry && hurry->next)
	{
		slowly = slowly->next;
		hurry = hurry->next->next;
		if (slowly == hurry)
			return (1);
	}
	return (0);
}
