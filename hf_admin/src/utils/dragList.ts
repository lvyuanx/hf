import { Ref, ref, watchEffect, onMounted } from 'vue';

interface Item {
  id: number | string;
  name: string;
}

const useDragList = <T extends Item>(listRef: Ref<HTMLElement | null>, listData: Ref<T[]>) => {
  const dragSrcEl: Ref<HTMLElement | null> = ref(null);

  const handleDragStart = (event: DragEvent) => {
    const target = event.target as HTMLElement;

    dragSrcEl.value = target;
    event.dataTransfer!.effectAllowed = 'move';
    event.dataTransfer!.setData('text/html', target.innerHTML);
  };


  const handleDragOver = (e: DragEvent) => {
    if (e.preventDefault) {
      e.preventDefault();
    }
    e.dataTransfer!.dropEffect = 'move';
    return false;
  };

  const handleDrop = (event: DragEvent) => {
    event.preventDefault();

    const target = event.target as HTMLElement;

    // 添加非空断言运算符
    if (dragSrcEl.value && listRef.value) {
      if (dragSrcEl.value !== target) {
        dragSrcEl.value.innerHTML = target.innerHTML;
        target.innerHTML = event.dataTransfer!.getData('text/html');

        const oldIndex = Array.prototype.indexOf.call(
          listRef.value.children,
          dragSrcEl.value as HTMLElement,
        );
        const newIndex = Array.prototype.indexOf.call(
          listRef.value.children,
          target as HTMLElement,
        );

        const movingItem = listData.value.splice(oldIndex, 1)[0];
        listData.value.splice(newIndex, 0, movingItem);
      }
    }

    event.stopPropagation();
  };


  return {
    handleDragStart, handleDragOver, handleDrop
  }


};

export default useDragList;
