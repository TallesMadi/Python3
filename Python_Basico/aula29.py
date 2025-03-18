"""
CONSTANTE = "Variáveis" que não vão mudar
Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)
"""
#variaveis
velocidade = 61  # velocidade atual do carro
local_carro = 100  # local em que o carro está na estrada

#constantes
RADAR_1 = 60  # velocidade máxima do radar 1
LOCAL_1 = 100  # local onde o radar 1 está
RADAR_RANGE = 1  # A distância onde o radar pega

velocidade_Carro_radar_1 = velocidade > RADAR_1
primeiro_range_radar_1 = LOCAL_1 - RADAR_RANGE
ultimo_range_radar_1 = LOCAL_1 + RADAR_RANGE
carro_passou_radar_1 = primeiro_range_radar_1 <= local_carro <= ultimo_range_radar_1
carro_multado = carro_passou_radar_1 and velocidade_Carro_radar_1

if carro_multado: 
    print('Você excedeu o limite de velocidade do Radar 1')
else:
    print('Você não excedeu o limite de velocidade do Radar 1')

    
    



