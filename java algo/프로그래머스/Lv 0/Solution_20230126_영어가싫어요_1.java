public class Solution_20230126_영어가싫어요_1 {

    public long solution1(String numbers) {
        long answer = 0;

        numbers=numbers.replaceAll("zero","0");
        numbers=numbers.replaceAll("one","1");
        numbers=numbers.replaceAll("two","2");
        numbers=numbers.replaceAll("three","3");
        numbers=numbers.replaceAll("four","4");
        numbers=numbers.replaceAll("five","5");
        numbers=numbers.replaceAll("six","6");
        numbers=numbers.replaceAll("seven","7");
        numbers=numbers.replaceAll("eight","8");
        numbers=numbers.replaceAll("nine","9");

        return Long.parseLong(numbers);
    }

    public long solution2(String numbers) {
        long answer = 0;
        String[] num = {"zero","one","two","three","four","five","six","seven","eight","nine"};
        for(int i = 0; i < num.length; i++){
            numbers = numbers.replace(num[i], Integer.toString(i));
        }
        answer = Long.parseLong(numbers);
        return answer;
    }
}
