var cases = new (string? Value, bool Expected)[] {
(null, false), ("", false), ("A123456789", true), ("a123456789", true),
("A123456788", false), ("A123456798", true), ("Z987654321", false),
("0123456789", false), ("A323456789", false), ("A12345x789", false),
("A１２３４５６７８９", false), (" A123456789", false), ("A123456789 ", false)
};
foreach (var item in cases)
{
    var actual = IsValidTaiwanId(item.Value);
    if (actual != item.Expected) throw new Exception($"Unexpected result for {item.Value}");
}
Console.WriteLine($"PASS: {cases.Length} format/checksum cases, including the equal-weight swap limitation.");
static bool IsValidTaiwanId(string? id)
{
    // 1. 基本檢查
    if (string.IsNullOrEmpty(id) || id.Length != 10)
    {
        return false;
    }
    // 2. 統一轉成大寫
    id = id.ToUpperInvariant();
    // 3. 英文字母對應的地區代碼
    Dictionary<char, int> letterCodes = new()
    {
        ['A'] = 10,
        ['B'] = 11,
        ['C'] = 12,
        ['D'] = 13,
        ['E'] = 14,
        ['F'] = 15,
        ['G'] = 16,
        ['H'] = 17,
        ['I'] = 34,
        ['J'] = 18,
        ['K'] = 19,
        ['L'] = 20,
        ['M'] = 21,
        ['N'] = 22,
        ['O'] = 35,
        ['P'] = 23,
        ['Q'] = 24,
        ['R'] = 25,
        ['S'] = 26,
        ['T'] = 27,
        ['U'] = 28,
        ['V'] = 29,
        ['W'] = 32,
        ['X'] = 30,
        ['Y'] = 31,
        ['Z'] = 33
    };
    // 4. 第一碼必須是合法英文字母
    char letter = id[0];
    if (!letterCodes.TryGetValue(letter, out int letterCode))
    {
        return false;
    }
    // 5. 第二碼只能是 1 或 2
    if (id[1] != '1' && id[1] != '2')
    {
        return false;
    }
    // 6. 後面 9 碼必須全部是數字
    int[] numbers = new int[9];
    for (int i = 1; i < id.Length; i++)
    {
        if (id[i] < '0' || id[i] > '9')
        {
            return false;
        }
        numbers[i - 1] = id[i] - '0';
    }
    // 7. 把地區碼拆成兩位數
    int firstDigit = letterCode / 10;
    int secondDigit = letterCode % 10;
    // 8. 身分證各數字的權重
    int[] weights =
    {
        8, 7, 6, 5, 4, 3, 2, 1, 1
    };
    // 9. 計算 checksum
    int sum = 0;
    sum += firstDigit * 1;
    sum += secondDigit * 9;
    for (int i = 0; i < numbers.Length; i++)
    {
        sum += numbers[i] * weights[i];
    }
    // 10. 可以被 10 整除就通過
    return sum % 10 == 0;
}
