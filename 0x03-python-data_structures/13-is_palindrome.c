#include "lists.h"
#include <stddef.h>

int is_palindrome(listint_t **head);
listint_t *reverse_listint(listint_t **head);

/**
 * reverse_listint - reverses part of a linked list to give a mirror image
 * @head: pointer to pointer
 * Return: pointer to head
 */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *node = *head, *next, *previous = NULL;

	while (node)
	{
		next = node->next;
		node->next = previous;
		previous = node;
		node = next;
	}
	*head = previous;
	return (*head);
}

/**
 * is_palindrome - checks if a sinly linked list is a palindrome
 * @head: pointer to pointer
 * Return: 1 on success and 0 on failure
 */
int is_palindrome(listint_t **head)
{
	listint_t *temp, *reverse, *middle;
	size_t size = 0, i;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	temp = *head;
	while (temp)
	{
		size++;
		temp = temp->next;
	}
	temp = *head;
	for (i = 0; i < (size / 2) - 1; i++)
		temp = temp->next;
	if ((size % 2) == 0 && temp->n != temp->next->n)
		return (0);
	temp = temp->next->next;
	reverse = reverse_listint(&temp);
	middle = reverse;

	temp = *head;
	while (reverse)
	{
		if (temp->n != reverse->n)
			return (0);
		temp = temp->next;
		reverse = reverse->next;
	}
	reverse_listint(&middle);

	return (1);
}
