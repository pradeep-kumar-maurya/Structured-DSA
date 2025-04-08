def m(arr, ans):

	for i in arr:
	
		if not isinstance(i, list):
			ans.append(i)
		
		else:
			m(i, ans)

	return ans


print(m([1,2,[3,4,[5,6,[7]]]], []))
print(m([1,"2",[3.01,4.99,[5,6,[7]]]], []))
