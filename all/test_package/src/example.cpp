/**
 * @file example.cc
 * @author Mergim Halimi (m.halimi123@gmail.com)
 * @brief This file contains an example for using the Object Interface class.
 * @version 0.1
 * @date 2023-04-18
 *
 * @copyright Copyright (c) 2023, MassCalculator, Org., All rights reserved.
 * @license This project is released under the  MIT license (MIT).
 *
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to deal
 * in the Software without restriction, including without limitation the rights
 * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included in
 * all copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
 * SOFTWARE.
 */
#include "masscalculator/masscalculator-core/interface/object_interface.h" // for Object<T, U>
#include "masscalculator/masscalculator-core/materials/constants/alloy_coppers.h" // for alloycopper::k*
#include "masscalculator/masscalculator-core/materials/materials.hh" // for Materials*
#include "masscalculator/masscalculator-core/shapes/shapes.hh" // for Shapes*
#include "masscalculator/third_party/units/units.h"            // for units::*

#include <memory> // for std::make_unique

// NOLINTNEXTLINE(google-global-names-in-headers,google-build-using-namespace)
using namespace units::literals;

int main() {
  /**
   * @brief Create a unique_ptr for the shape, giving it the properties of the
   * shape. E.g.: A cylinder with properties: Radius 0 and Length 0.
   */
  std::unique_ptr<masscalculator::core::shapes::Shape<
      masscalculator::core::shapes::Cylinder>>
      shape = std::make_unique<masscalculator::core::shapes::Cylinder>(0.0_m,
                                                                       0.0_m);

  /**
   * @brief Create a unique_ptr for the material, giving it the properties of
   * the material. E.g.: An Alloy Copper with properties: Type 194Iron.
   */
  std::unique_ptr<masscalculator::core::materials::Material<
      masscalculator::core::materials::AlloyCoppers>>
      material = std::make_unique<
          masscalculator::core::materials::AlloyCoppers>(
          masscalculator::core::materials::constants::alloycopper::k194Iron);

  /**
   * @brief Create a unique_ptr for the object, giving it the properties of
   * the object. E.g.: The shape and material constructed earlier.
   */
  std::unique_ptr<masscalculator::core::interface::Object<
      masscalculator::core::shapes::Shape<
          masscalculator::core::shapes::Cylinder>,
      masscalculator::core::materials::Material<
          masscalculator::core::materials::AlloyCoppers>>>
      object = std::make_unique<masscalculator::core::interface::Object<
          masscalculator::core::shapes::Shape<
              masscalculator::core::shapes::Cylinder>,
          masscalculator::core::materials::Material<
              masscalculator::core::materials::AlloyCoppers>>>(shape, material);

  return EXIT_SUCCESS;
}
