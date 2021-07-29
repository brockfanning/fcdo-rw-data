from sdg.open_sdg import open_sdg_build

def alter_meta(meta):
    if 'en' in meta:
        for key in meta['en']:
            if meta['en'][key] is not None and isinstance(meta['en'][key], str):
                meta['en'][key] = meta['en'][key].replace("'", "&#39;")
    for key in meta:
        if meta[key] is not None and isinstance(meta[key], str):
            meta[key] = meta[key].replace("'", "&#39;")

    return meta

def alter_data(df):
    def row_matches_ref_area(row):
        return row['REF_AREA'] == 'RW'

    df = df.copy()
    mask = df.apply(row_matches_ref_area, axis=1)
    return df[mask]

open_sdg_build(config='config_data.yml', alter_meta=alter_meta, alter_data=alter_data)
