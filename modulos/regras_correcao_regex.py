regras_de_correcao_regex = {
    'CDS Ficha de Atendimento Domiciliar': [
        (r'atendimentosdomiciliares.*são idênticos', 'Ficha CDS Domiciliar da data ( ) do profissional ( ) com paciente ( ) duplicado.')
    ],
    'CDS Ficha de Atendimento Individual': [
        (r'atendimentosindividuais.*são idênticos', 'Ficha CDS da data ( ) da profissional ( ) com duplicidade de paciente ( ).'),
        (r'ciaps.*abp022', 'Ficha CDS da data ( ) da profissional ( ), paciente () está com um CIAPS exclusivo de sexo feminino mas o cadastro do paciente está registrado como sendo do sexo MASCULINO.'),
        (r'profissionalcns possui um valor inválido', 'Atendimento Individual → Profissional CNS inválido. Verifique o CNES atualizado.'),
        (r'cbocodigo_2002', 'CBO ( ) do profissional ( ) possui um valor inválido.'),
        (r'outrociap1.*y14', 'O CIAP ( ) na ficha CDS da data ( ) da profissional ( ) precisa ser preenchido como CIAP2.')
    ],
    'CDS Ficha de Atendimento Odontológico': [
        (r'atendimentosodontologicos.*são idênticos', 'Ficha CDS odontologico da profissional ( ) da data ( ), está com pacientes duplicados.')
    ],
    'CDS Ficha de Atividade Coletiva': [
        (r'temasparasaude', 'Atividade Coletiva ( ). É necessário marcar um TEMA e uma PRÁTICA.'),
        (r'cpf.*obrigatório', 'Possível bug no sistema, pois na Atividade em Grupo () da profissional (), todos os participantes possuem ao menos um dos documentos.'),
        (r'inep', 'Na Atividade Coletiva ( ). Caso a atividade não seja efetuado em uma escola, campo de programa saúde na escola e numero INEP não precisão ser alterados, por favor corrigir esses pontos.')
    ],
    'CDS Ficha de Cadastro Domiciliar': [
        (r'enderecolocalpermanencia.*numero.*letras.*dígitos', 'Código de Domicílio ( ). O número do domicílio está registrado de maneira errada (S]N), o correto é (SN).')
    ],
    'CDS Ficha de Cadastro Individual': [
        (r'codigoibgemunicipionascimento.*9999996', 'No cadastro do paciente ( ), o campo Cidade Nascimento está marcado com uma opção escrito NÃO USAR. É necessário colocar a cidade de nascimento correta.'),
        (r'orientacaosexualcidadao.*obrigatório', 'No cadastro do paciente (), o campo Desejo Informar Orientação Sexual está marcado como SIM, mas não foi registrado qual opção seria.')
    ],
    'CDS Ficha de Procedimentos': [
        (r'datahorafinalatendimento.*anterior à data de atendimento', 'Profissional ( ) preencheu, na ficha CDS de Procedimentos da data ( ), na hora de início do atendimento um horário maior que a hora de término do atendimento.'),
        (r'profissionalcns possui um valor inválido', 'Procedimentos → Profissional CNS inválido. Verifique o CNES atualizado.')
    ]
}
