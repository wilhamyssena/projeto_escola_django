from django.db import models


class Base(models.Model):
    data_criacao = models.DateTimeField(auto_now_add=True,
                                        db_column='t____criacao',
                                        db_comment='Data da inclusão do objeto')

    data_atualizacao = models.DateTimeField(auto_now_add=True,
                                            db_column='t____ulat',
                                            db_comment='Data de atualização do objeto')

    ativo = models.BooleanField(default=True,
                                db_column='____ativo',
                                db_comment='Indicador se o objeto ainda está ativo')

    class Meta:
        abstract = True



