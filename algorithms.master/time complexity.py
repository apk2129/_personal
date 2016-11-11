\Lists:
                               Complexity
Operation     | Example      | Class         | Notes
--------------+--------------+---------------+-------------------------------
'Index'         | l[i]         | O(1)	     |
'Store'         | l[i] = 0     | O(1)	     |
'Length'        | len(l)       | O(1)	     |
'Append'        | l.append(5)  | O(1)	     |
'Pop'	          | l.pop()      | O(1)	     | same as l.pop(-1), popping at end
'Clear'         | l.clear()    | O(1)	     | similar to l = []




\Sets:
                               Complexity
Operation     | Example      | Class         | Notes
--------------+--------------+---------------+-------------------------------
'Length'        | len(s)       | O(1)	     |
'Add'           | s.add(5)     | O(1)	     |
'Containment'   | x in/not in s| O(1)	     | compare to list/tuple - O(N)
'Remove'        | s.remove(5)  | O(1)	     | compare to list/tuple - O(N)
'Discard'       | s.discard(5) | O(1)	     |
'Pop'           | s.pop(i)     | O(1)	     | compare to list - O(N)
'Clear'         | s.clear()    | O(1)	     | similar to s = set()


\Dictionaries: dict and defaultdict
                               Complexity
Operation     | Example      | Class         | Notes
--------------+--------------+---------------+-------------------------------
'Index'         | d[k]         | O(1)	     |
'Store'         | d[k] = v     | O(1)	     |
'Length'        | len(d)       | O(1)	     |
'Delete'        | del d[k]     | O(1)	     |
'get/setdefault'| d.method     | O(1)	     |
'Pop'           | d.pop(k)     | O(1)	     |
'Pop item'      | d.popitem()  | O(1)	     |
'Clear'         | d.clear()    | O(1)	     | similar to s = {} or = dict()
'Views'         | d.keys()     | O(1)	     |
