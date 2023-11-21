from datasets import load_dataset, Dataset


class HFPTDataLoader:
    def __init__(self, dataset_name: str):
        self.dataset_name = dataset_name

    def create_dataset(self, split: str = "train") -> Dataset:
        dataset = load_dataset(self.dataset_name, split=split)
        # def process(rec):
        #     human_reference = rec["prompt"]
        #     meaning_representation = rec["response"]
        #     return {
        #         "text": f"""<s>[INST] <<SYS>>Extract entities from the text given below.<</SYS>> {human_reference} [/INST] </s><s>[INST] {meaning_representation} [/INST]"""
        #     }
        # dataset = dataset.map(process, remove_columns=["prompt", "response"]).shuffle()
        return dataset
