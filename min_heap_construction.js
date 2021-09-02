class MinHeap {
  constructor(array) {
    this.heap = this.buildHeap(array);
  }

  buildHeap(array) {
    const parIdx = Math.floor((array.length - 2) / 2);
    for (let idx = parIdx; idx >= 0; idx--) {
      this.siftDown(idx, array.length - 1, array);
    }
    return array;
  }

  siftDown(curIdx, endIdx, heap) {
    let firstChildIdx = curIdx * 2 + 1;
    while (firstChildIdx <= endIdx) {
      let secondChildIdx = curIdx * 2 + 2 <= endIdx ? curIdx * 2 + 2 : -1;
      let idxSwap;
      if (secondChildIdx !== -1 && secondChildIdx < firstChildIdx) {
        idxSwap = secondChildIdx;
      } else {
        idxSwap = firstChildIdx;
      }
      if (heap[idxSwap] < heap[curIdx]) {
        this.swap(dxSwap, curIdx, heap);
        curIdx = idxSwap;
        firstChildIdx = curIdx * 2 + 1;
      } else {
        return;
      }
    }
  }

  siftUp(curIdx, heap) {
    let parIdx = Math.floor((curIdx - 1) / 2);
    while (parIdx >= 0 && heap[parIdx] > heap[curIdx]) {
      this.swap(parIdx, curIdx, heap);
      curIdx = parIdx;
      parIdx = Math.floor((curIdx - 1) / 2);
    }
  }

  remove() {
    this.swap(0, this.heap.length - 1, this.heap);
    const valToRemove = this.heap.pop();
    this.siftDown(0, this.heap.length - 1, this.heap);
    return valToRemove;
  }

  insert(value) {
    this.heap.push(value);
    this.siftUp(this.heap.length - 1, this.heap);
  }

  peek() {
    return this.heap[0];
  }

  swap(i, j, heap) {
    const temp = heap[j];
    heap[j] = heap[i];
    heap[i] = temp;
  }
}
