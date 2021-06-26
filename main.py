import os
import sys


sys.path.append(os.getcwd())

import comet.src.data.config as cfg
import comet.src.interactive.functions as interactive
from openie import StanfordOpenIE

if __name__ == '__main__':
    #model_path = 'comet/model/atomic_pretrained_model.pickle'
    model_path = 'trained_models/my_model_v8.pickle'
    opt, state_dict = interactive.load_model_file(model_path)

    data_loader, text_encoder = interactive.load_data("conceptnet",opt)

    n_ctx = data_loader.max_e1 + data_loader.max_e2 + data_loader.max_r

    n_vocab = len(text_encoder.encoder) + n_ctx
    model = interactive.make_model(opt,n_vocab,n_ctx,state_dict)

    cfg.device = "cpu"



    input_event= 'feline'
    category = 'all'
    sampling_algorithm = 'topk-5'

    sampler = interactive.set_sampler(opt,sampling_algorithm,data_loader)

    output = interactive.get_conceptnet_sequence(input_event,model,sampler,data_loader,text_encoder,category)

    
    print(output['IsHypernymOf'])
    print(output['IsHyponymOf'])

    input_event = 'cat'
    output = interactive.get_conceptnet_sequence(input_event,model,sampler,data_loader,text_encoder,category)

    print(output['IsHypernymOf'])
    print(output['IsHyponymOf'])

    client = StanfordOpenIE()
    text = 'Barack Obama was born in Hawaii.'

    triples = client.annotate(text)

    input_event = triples[0]['subject']

    output = interactive.get_conceptnet_sequence(input_event,model,sampler,data_loader,text_encoder,category)

    print(output['IsHypernymOf'])
    print(output['IsA'])

    for triple in triples:
        print('|-', triple)
    
