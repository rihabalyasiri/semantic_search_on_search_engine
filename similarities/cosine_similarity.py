from sentence_transformers import util
import torch


def calculate_similarity(ad_vector: list, query_vector: list):

    ad_tensor = torch.tensor(ad_vector)
    query_tensor = torch.tensor(query_vector)

    sim = util.cos_sim(ad_tensor, query_tensor)

    return sim.item()

