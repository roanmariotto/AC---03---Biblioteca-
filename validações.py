def validar_titulo(titulo):
    ## verificar se o titulo esta vazio 

    return titulo and titulo.strip() != " "

def validar_categoria(categoria): 

    ## verificar se esta em uma das categorias da lista 

    categorias_validas = [ "Romance" , "Terror" , "Suspense" , "Bibliografia" , "Acao" , "Inlges" , "Educativo" ]
    return categoria.tittle() in categorias_validas 

    if not categoria_input or not categoria_input.strip():
        return False
    
    categoria_formatada = categoria_input.strip().title()       # deixa a 1ª letra maiúscula
    
    return categoria_formatada in categorias_permitidas
