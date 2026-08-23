# Respostas do LAB 01

Nome: Nícolas Silva Maciel e Murilo Amorim
Matricula: 26128017
Dupla (M2 em diante):

---

## M2 - Quem quebrou o painel

**Hash curto do commit que introduziu o erro: f0cf14e**

**Autor: Nicolas-S-Maciel <sesinick@gmail.com>**

**Data: Sun Aug 16 16:43:54 2026 -0300**

**Linha alterada (antes e depois):**

```
antes: -0,0 +1
depois: -0,0 +1
```

---

## M3 - O segredo vazado

**O que voce esperava ver no `git status` e o que apareceu: Esperava que apareceria diretamente mostrando o credenciais env no gitignore, mas acabou mostrando as pastas necessárias para selecionar antes de mostrar o status de uma especifica**

**Depois do push, alguem que clonar o repositorio ainda consegue ler a chave?Responda em duas linhas, explicando o motivo: Sim, na minha visão é possível ler a chave. Porém o histórico de commits anteriores do Git ainda armazena o arquivo original contendo a credencial exposta.**

---

## M4 - Colisao

**O que significavam os marcadores que apareceram dentro do arquivo:**

- `<<<<<<<` : Indica o início do trecho conflituoso que estava na sua branch atual
- `=======` : Funciona como a linha divisória que separa o seu código do código que já estava presente na branch de destino.
- `>>>>>>>` : Indica o final do trecho conflitante vindo da branch principal/remota.

**Qual pedaco veio de quem, e qual titulo voces decidiram manter: Meu pedaço foi para o Murilo, e decidimos manter o titulo**

---

## Casa - Incidente na linha 3

**Hash do commit que quebrou o painel: f0cf14e**

**Hash do commit de revert: 5d83f1b**

**Por que `git revert` e nao `git reset` neste caso: Porque o git revert cria um novo commit desfazendo as alterações, mantendo intacto o histórico oficial do repositório / Já o git reset apaga ou reescreve o histórico de commits**
