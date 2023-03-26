#!/bin/bash

# função para aguardar a tecla 'K'
function wait_for_k {
  read -n 1 -r -s -p $'Pressione a tecla "K" para retornar ao menu...\n' key
  while [ "$key" != "K" ] && [ "$key" != "k" ]; do
    read -n 1 -r -s -p $'Pressione a tecla "K" para retornar ao menu...\n' key
  done
  echo ""
}

# loop principal do menu
while true; do
  clear
  echo "Escolha um script:"
  echo "1. bin2string.py"
  echo "2. bincypher.py"
  echo "3. obfuscator.py"
  echo "4. string2bin.py"
  echo "0. Sair"

  read choice
  case $choice in
    1)
      clear
      echo "Rodando bin2string.py..."
      python3 bin2string.py
      wait_for_k
      ;;
    2)
      clear
      echo "Rodando bincypher.py..."
      python3 bincypher.py
      wait_for_k
      ;;
    3)
      clear
      echo "Rodando obfuscator.py..."
      python3 obfuscator.py
      wait_for_k
      ;;
    4)
      clear
      echo "Rodando string2bin.py..."
      python3 string2bin.py
      wait_for_k
      ;;
    0)
      clear
      echo "Saindo..."
      exit 0
      ;;
    *)
      clear
      echo "Opção inválida!"
      wait_for_k
      ;;
  esac
done

