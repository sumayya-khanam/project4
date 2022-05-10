
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view(['POST'])
def isanagram(request):
    w1 = request.POST.get('w1')
    w2 = request.POST.get('w2')
    w1=w1.replace(" ","")
    w2=w2.replace(" ","")
    l1 =[x for x in  w1.lower()]
    l2 =[x for x in w2.lower()]
    print(l1,end = "\n")
    print(l2)
    l1.sort()
    l2.sort()
    if l1 == l2:
        status="The strings are anagrams"
    else:
        status="The strings are not anagrams"
    return Response(status)


@api_view(['POST'])
def isPalindrome(request):
    string=request.POST.get('string')
    string=string.lower()
    string=string.replace(" ","")
    
    reverse_string=string[::-1]
    if reverse_string == string:
        status="The string is palindrome"
    else:
        status="The string is not a palindrome"
    return Response(status)        
        
    
   
   
    
    
    
            
        
            