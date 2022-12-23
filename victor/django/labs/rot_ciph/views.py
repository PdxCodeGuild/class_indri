from django.shortcuts import render

# Create your views here.
# Home Page
def index(request):
    

    return render(request, 'rot_ciph/index.html')

def encrypt(request):
    ALPHABET = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    output = ""
    phrase = request.POST['phrase']
    shift = int(request.POST['shift'])
    shift = shift % 26
    for char in phrase:
        if char in ALPHABET:
            position = ALPHABET.index(char)
            new_position = position + shift
            output += ALPHABET[new_position]
            
    context = {"output": output}
    return render(request, 'rot_ciph/results.html', context)
