def sort_steps(steps):
    """
    对步骤数据列表进行排序，并返回排好序的列表。

    Args:
        steps (list): 包含步骤数据的字典列表

    Returns:
        list: 排好序的步骤数据列表
    """
    # 定义一个函数，获取指定 ID 的 step 对象
    def get_step_obj(step_id):
        for step in steps:
            if step.id == step_id:
                return step
        return None

    # 使用 sorted() 函数对列表进行排序
    sorted_lst = sorted(steps, key=lambda x: x.parent_step_id if x.parent_step_id is not None else -1)

    # 遍历排好序的列表，并比较每个元素和它的前驱 step_base 的大小关系
    result_lst = []
    for step in sorted_lst:
        parent_id = step.parent_step_id
        if parent_id is None:
            # 处理第一个元素
            result_lst.append(step)
        else:
            parent_step = get_step_obj(parent_id)
            if parent_step is not None:
                if parent_step.step_base <= step.step_base:
                    result_lst.append(step)
            else:
                result_lst.append(step)

    return result_lst



def sort_ser_steps(steps):
    """
    对步骤数据列表进行排序，并返回排好序的列表。

    Args:
        steps (list): 包含步骤数据的字典列表

    Returns:
        list: 排好序的步骤数据列表
    """
    # 定义一个函数，获取指定 ID 的 step 对象
    def get_step_obj(step_id):
        for step in steps:
            if step['id'] == step_id:
                return step
        return None

    # 使用 sorted() 函数对列表进行排序
    sorted_lst = sorted(steps, key=lambda x: x['parent_step_id'] if x['parent_step_id'] is not None else -1)

    # 遍历排好序的列表，并比较每个元素和它的前驱 step_base 的大小关系
    result_lst = []
    for step in sorted_lst:
        parent_id = step['parent_step_id']
        if parent_id is None:
            # 处理第一个元素
            result_lst.append(step)
        else:
            parent_step = get_step_obj(parent_id)
            if parent_step is not None:
                if parent_step['step_base'] <= step['step_base']:
                    result_lst.append(step)
            else:
                result_lst.append(step)

    return result_lst

