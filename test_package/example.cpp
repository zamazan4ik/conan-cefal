#include <cefal/cefal>

#include <list>
#include <vector>

int main()
{
    std::list<std::vector<int>> result =
    cefal::unit<std::vector>(3) | cefal::ops::map          ([](int x) { return ops::unit<std::vector>(x); })
                                | cefal::ops::innerFilter  ([](int x) { return x % 2; })
                                | cefal::ops::innerFlatMap ([](int x) { return std::vector{x + 1, x + 2}; })
                                | cefal::ops::innerMap     ([](int x) { return x * 3; })
                                | cefal::ops::as<std::list>();
  return 0;
}
