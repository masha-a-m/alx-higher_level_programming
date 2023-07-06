#!/bin/bash
#technical interview preparation


if list_of_integers is None or list_of_integers == []:
        return None
    lo = 0
    hi = len(list_of_integers)
	     if mid > 0 and list_of_integers[mid] < list_of_integers[mid + 1]:
        return find_peak(list_of_integers[mid:])
    if mid > 0 and list_of_integers[mid] < list_of_integers[mid - 1]:
        return find_peak(list_of_integers[:mid])
