from src.db_controller import get_one_data


class Pokemon:
    def __init__(self, id_, no, name, type1, type2, version1, version2):
        self.id_ = id_
        self.no = no
        self.name = name
        self.type1 = type1
        self.type2 = type2
        self.version1 = version1
        self.version2 = version2

    def __repr__(self):
        return 'id: {} No: {} name: {} type1: {} type2: {} version1: {} version2: {}'.format(self.id_, self.no, self.name, self.type1, self.type2, self.version1, self.version2)


def get_pokemon(n, options):
    result = []
    nos = []
    types = []
    while len(result) < n:
        row = get_one_data()
        p = Pokemon(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
        # 重複があるかどうか
        if p.no in nos:
            continue
        # 剣のみ
        if 'sword' in options:
            if p.version1 == '盾':
                continue
        # 盾のみ
        if 'shield' in options:
            if p.version1 == '剣':
                continue
        # 御三家なし
        if 'first' in options:
            if p.version1 == '御三家':
                continue
        # 伝説なし
        if 'legend' in options:
            if p.version2 == '伝説':
                continue
        # ガラルのみ
        if 'gallant' in options:
            if p.version2 == 'ガラル':
                continue
        # タイプ一致ではない場合
        if 'type' in options:
            if p.type1 in types or p.type2 in types:
                continue
        result.append(p)
        nos.append(p.no)
        types.append(p.type1)
        if p.type2 != '':
            types.append(p.type2)

    return result
