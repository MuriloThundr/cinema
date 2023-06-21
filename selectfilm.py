print('*********************************************************************')
print('***************************MOVIE THEATER*****************************')
print('*********************************************************************')


listaFilmes = []
escolha = 0
totalIngresso = 60


while(escolha != 7):
    print("1. Adicionar filme")
    print("2. Remover filme")
    print("3. Buscar filme")
    print("4. Edtiar filme")
    print("5. Vender Ingresso")
    print('6. Listar filme')
    print("7. Sair")
    escolha = int(input('Opção: '))

    if escolha == 1:
        print("Qual filme você deseja adicionar?")
        filme = input().upper().strip()
        listaFilmes.append(filme)
    if escolha == 2:
        print("Qual filme você deseja remover?")
        filme = input().upper().strip()
        listaFilmes.remove(filme)
        for item in listaFilmes:
            if filme == item:
                print("filme: ", item)
    if escolha == 3:
        print("Qual filme você deseja buscar?")
        filme = input().upper().strip()
    if escolha == 4:
        print("Qual filme você deseja editar?")
        filme = input().upper().strip()
    if escolha == 5:
        print("Qual filme você deseja vender?")
        qtdIngresso = (input())
        if  qtdIngresso > totalIngresso:
            print("Sala de video cheia")
        else:
            ingresso = totalIngresso - qtdIngresso
            print("Ainda restam: ", ingresso) 
    if escolha == 6:
        print("Lista dos filmes adicionados:", listaFilmes)
        
    if escolha == 7:
        print("Saindo do sistema...")

        input()
        os.system("cls")



    
