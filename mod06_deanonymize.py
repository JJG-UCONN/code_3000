import pandas as pd

def load_data(anonymized_path, auxiliary_path):
    """
    Load anonymized and auxiliary datasets.
    """
    anon = pd.read_csv(anonymized_path)
    aux = pd.read_csv(auxiliary_path)
    return anon, aux


def link_records(anon_df:pd.DataFrame, aux_df:pd.DataFrame):
    """
    Attempt to link anonymized records to auxiliary records
    using exact matching on quasi-identifiers.

    Returns a DataFrame with columns:
      anon_id, matched_name
    containing ONLY uniquely matched records.
    """
    retVal = {"anon_id": [], "matched_name": []}
    
    for idx, row in anon_df.iterrows():
        #iterate through each anonymous element
        #now determine if exists in aux_df
        for idx2, row2, in aux_df.iterrows():
            #if (row.values[1:] == row.values[1:]):
            if (row["age"] == row2["age"]) and (row["zip3"] == row2["zip3"]) and (row["gender"] == row2["gender"]):
                retVal["anon_id"].append(row["anon_id"])
                retVal["matched_name"].append(row2["name"])
                anon_df = anon_df.drop(idx)
                aux_df = aux_df.drop(idx2)

                break    
    return pd.DataFrame(retVal)
    #retVal = {"anon_id": anon_df.pop("anon_id"), "matched_name": aux_df.pop("name")}
    #return pd.DataFrame(retVal)
    #raise NotImplementedError


def deanonymization_rate(matches_df:pd.DataFrame, anon_df:pd.DataFrame):
    """
    Compute the fraction of anonymized records
    that were uniquely re-identified.
    """
    totalMatches = matches_df.size / matches_df.columns.size
    allPoss = anon_df.size / anon_df.columns.size
    return (totalMatches / allPoss)
    #raise NotImplementedError
