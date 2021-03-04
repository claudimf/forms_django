from django.shortcuts import render
from passagens.forms import PassagemForms, PessoaForms


def index(request):
    form = PassagemForms()
    pessoa_form = PessoaForms()
    context = {'form': form, 'pessoa_form': pessoa_form}
    return render(request, 'index.html', context)


def revisao_consulta(request):
    if request.method == 'POST':
        form = PassagemForms(request.POST)
        pessoa_form = PessoaForms(request.POST)
        context = {'form': form, 'pessoa_form': pessoa_form}

        if form.is_valid():
            return render(request, 'minha_consulta.html', context)
        else:
            print('Form inválido')
            return render(request, 'index.html', context)
