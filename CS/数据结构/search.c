/*
 * @Author: 崩布猪
 * @Date: 2024-07-04 17:24:17
 * @LastEditors: 崩布猪
 * @LastEditTime: 2024-07-04 20:33:58
 * @FilePath: \数据结构\search.c
 * @Description: 
 * 
 */

int binarySearch(int arr[],int size,int target){
    int left =0;
    int right = size - 1;
    while(left <= right)
    {
        int mid = left + (right - left)/2;
        if (arr[mid] < target){
            left = mid + 1;
        }else if (arr[mid] > target){
            right = mid - 1;
        }else{
            return mid;
        }

    return -1;
    }
}

int main(){
    int arr[] = {0,1,2,3,4,5,6,7,8,9};
    int size = 10;
    int target = 5;
    printf(binarySearch(arr,size,target))
}