# Program_Life
## 总体设计
基于康威生命游戏逻辑，一个方格如果围绕它的8个cell中有3个cell存活，则下一回合存活，如果一个存活cell周围没有2个或3个cell存活，则死亡

另加入了cell规模系统，如果一个存活cell周围有3个cell存活，则可以提升规模。显示为RGB参数更大了。相对的，如果存活cell周围没有2个或3个存活cell，则减小规模，显示为RGB参数变小了。如果参数变为0，则cell死亡

RGB有三个参数（Red，Green，Blue），最高都为255，最低为0

## 操作方法
基于pygame设计UI
点击START开始模拟，点击STOP暂停
左键单击添加cell，再单击去除cell
如果按住SHIFT左键拖动的话批量添加cell
右键拖动画布
上下滚轮放大缩小
