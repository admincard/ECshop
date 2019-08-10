import jsonpath

def get_result_one(data,keyword):
    """
    通过关键字获取对应的一个值
    :param data:数据源
    :param keyword:关键字
    :return:一个值
    """
    return jsonpath.jsonpath(data,f"$..{keyword}")[0]


def get_results_all(data,keyword):
    """
    通过关键字获取所有对应的值
    :param data: 数据源
    :param keyword: 关键字
    :return: list
    """
    return jsonpath.jsonpath(data,f"$..{keyword}")


def get_results_for_label_keyword(data,label,keyword):
    """
    通过上层的标签,获取关键字对应的所有数据
    :param data: 数据源
    :param label: 上层标签
    :param keyword: 关键字
    :return: list
    """
    return jsonpath.jsonpath(data,f"$..{label}[*].{keyword}")
if __name__ == '__main__':
    data = {
        "store": {
            "book": [
                {
                    "category": "reference",
                    "author": "Nigel Rees",
                    "title": "Sayings of the Century",
                    "price": 8.95
                },
                {
                    "category": "fiction",
                    "author": "Evelyn Waugh",
                    "title": "Sword of Honour",
                    "price": 12.99
                },
                {
                    "category": "fiction",
                    "author": "Herman Melville",
                    "title": "Moby Dick",
                    "isbn": "0-553-21311-3",
                    "price": 8.99
                },
                {
                    "category": "fiction",
                    "author": "J. R. R. Tolkien",
                    "title": "The Lord of the Rings",
                    "isbn": "0-395-19395-8",
                    "price": 22.99
                }
            ],
            "bicycle": {
                "color": "red",
                "price": 19.95
            }
        },
        "expensive": 10
    }
    # gr = GetResultEasy()
    # print(gr.get_result_for_keyword(data, 'color'))
    # # print(gr.get_results_for_keyword(data, 'price'))
    # print(gr.get_results_for_label_keyword(data, 'book', 'price'))