from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score

class Evaluator:

    def evaluate(self, trained_model, X_test, Y_test):
        ''' Faz uma predição e avalia o modelo. Poderia parametrizar o tipo de
            avaliação, entre outros.
        '''
        predictions = trained_model.predict(X_test)

        return (accuracy_score(Y_test, predictions),
                recall_score(Y_test, predictions, average='binary'),
                precision_score(Y_test, predictions, average='binary'),
                f1_score(Y_test, predictions, average='binary'))
