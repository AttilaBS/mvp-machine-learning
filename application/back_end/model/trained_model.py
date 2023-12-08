import numpy as np
import pickle


class TrainedModel:

    def load_trained_model(path):
        '''Carregamos o modelo treinado, no formato pickle.
        '''
        return pickle.load(open(path, 'rb'))

    def predictor(trained_model, form):
        '''Realiza a predição de um paciente com base no modelo treinado
        '''
        X_input = np.array([form.male,
                            form.age,
                            form.education,
                            form.current_smoker,
                            form.cigs_per_day,
                            form.bp_meds,
                            form.prevalent_stroke,
                            form.prevalent_hyp,
                            form.diabetes,
                            form.tot_chol,
                            form.sys_bp,
                            form.dia_bp,
                            form.bmi,
                            form.heart_rate,
                            form.glucose
                        ])
        # Faremos o reshape para que o modelo entenda que estamos passando
        diagnosis = trained_model.predict(X_input.reshape(1, -1))
        return int(diagnosis[0])
