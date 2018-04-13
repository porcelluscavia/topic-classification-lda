import os
from gensim.models.ldamodel import LdaModel
from time import time
import logging


class Model:
    """
    WRITTEN BY RYAN CALLIHAN
    """

    def __init__(self, num_categories=20, num_passes=1):
        self.num_categories = num_categories
        self.ldamodel = None
        self.num_passes = num_passes

    def create_model(self,
                     doc_matrix,
                     term_dictionary,
                     model_path,
                     save_model=True,
                     language='language_na'):
        """
        WRITTEN BY RYAN CALLIHAN
        Creates an LDA model based on a set of documents
        :param model_path:
        :param doc_matrix:
        :param term_dictionary:
        :param save_model:
        :param language:
        :return LDA model:
        """
        self.language = language
        start = time()
        self.ldamodel = LdaModel(doc_matrix,
                                 num_topics=self.num_categories,
                                 id2word=term_dictionary,
                                 passes=self.num_passes)

        if save_model:
            self.save_model(model_path=os.path.join(model_path,
                'models', self.language, '%s_%s_category_lda.model' % (language, str(self.num_categories))))

        logging.info('Training lasted: {:.2f}s'.format(time() - start))
        return self.ldamodel

    def load_model(self, model_path='lda.model'):
        """
        WRITTEN BY RYAN CALLIHAN
        Loads a pretrained LDA model
        :param model_path:
        :return LDA model:
        """
        return LdaModel.load(model_path)

    def save_model(self, model_path):
        """
        WRITTEN BY RYAN CALLIHAN
        Saves trained LDA model
        :param model_path:
        :return:
        """
        if not os.path.isdir('models'):
            os.mkdir('models')
        if not os.path.isdir(os.path.join('models', self.language)):
            os.mkdir(os.path.join('models', self.language))
        self.ldamodel.save(model_path)
        logging.info("Model Saved")
