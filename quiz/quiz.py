import random
import requests
from deep_translator import GoogleTranslator

class Quiz:
    def __init__(self):
        self.questions = []
        self.user_score = 0
        self.total_questions = 0

    def fetch_questions(self, num_questions=5):
        """Busca perguntas de uma API online e as traduz para português."""
        url = f"https://opentdb.com/api.php?amount={num_questions}&type=multiple"
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()

            for item in data['results']:
                question = GoogleTranslator(source='en', target='pt').translate(item['question'])
                incorrect_answers = [GoogleTranslator(source='en', target='pt').translate(ans) for ans in item['incorrect_answers']]
                correct_answer = GoogleTranslator(source='en', target='pt').translate(item['correct_answer'])

                options = incorrect_answers + [correct_answer]
                random.shuffle(options)

                correct_option_index = options.index(correct_answer) + 1

                self.add_question(question, options, correct_option_index)

        except requests.RequestException as e:
            print(f"Erro ao buscar perguntas: {e}")

    def add_question(self, question, options, correct_option):
        """Adiciona uma pergunta ao quiz."""
        if correct_option < 1 or correct_option > len(options):
            raise ValueError("A resposta correta deve ser um índice válido das opções.")
        self.questions.append({
            "question": question,
            "options": options,
            "correct_option": correct_option
        })

    def run_quiz(self):
        """Executa o quiz e calcula a pontuação do usuário."""
        print("Iniciando o Quiz!\n")
        self.user_score = 0
        self.total_questions = len(self.questions)

        questions_copy = self.questions[:]
        random.shuffle(questions_copy)

        for index, question_data in enumerate(questions_copy):
            print(f"Pergunta {index + 1}: {question_data['question']}")
            for i, option in enumerate(question_data['options'], start=1):
                print(f"{i}. {option}")

            while True:
                try:
                    answer = int(input("Sua resposta (escolha o número): "))
                    if 1 <= answer <= len(question_data['options']):
                        break
                    else:
                        print("Por favor, escolha uma opção válida.")
                except ValueError:
                    print("Entrada inválida. Digite um número.")

            if answer == question_data['correct_option']:
                print("Correto!\n")
                self.user_score += 1
            else:
                correct_ans = question_data['options'][question_data['correct_option'] - 1]
                print(f"Errado! A resposta correta era: {correct_ans}\n")

        self.show_statistics()

    def show_statistics(self):
        """Exibe os resultados e estatísticas do quiz."""
        print("Quiz Concluído!\n")
        print(f"Total de Perguntas: {self.total_questions}")
        print(f"Sua Pontuação: {self.user_score}/{self.total_questions}")
        print(f"Porcentagem: {(self.user_score / self.total_questions) * 100:.2f}%")


# Exemplo de uso
if __name__ == "__main__":
    quiz = Quiz()

    # Buscando perguntas online
    quiz.fetch_questions(num_questions=5)

    # Executando o quiz
    quiz.run_quiz()
