/*
 * Connection Rest API 1.0
 *
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.0
 * Generated by: https://github.com/openapitools/openapi-generator.git
 */


using System;
using System.Collections;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Linq;
using System.IO;
using System.Runtime.Serialization;
using System.Text;
using System.Text.RegularExpressions;
using Newtonsoft.Json;
using Newtonsoft.Json.Converters;
using Newtonsoft.Json.Linq;
using System.ComponentModel.DataAnnotations;
using OpenAPIDateConverter = IdeaStatiCa.ConnectionApi.Client.OpenAPIDateConverter;

namespace IdeaStatiCa.ConnectionApi.Model
{
    /// <summary>
    /// TextPosition
    /// </summary>
    [DataContract(Name = "TextPosition")]
    public partial class TextPosition : IValidatableObject
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="TextPosition" /> class.
        /// </summary>
        /// <param name="origin">origin.</param>
        /// <param name="angles">angles.</param>
        public TextPosition(List<double> origin = default(List<double>), List<double> angles = default(List<double>))
        {
            this.Origin = origin;
            this.Angles = angles;
        }

        /// <summary>
        /// Gets or Sets Origin
        /// </summary>
        [DataMember(Name = "origin", EmitDefaultValue = true)]
        public List<double> Origin { get; set; }

        /// <summary>
        /// Gets or Sets Angles
        /// </summary>
        [DataMember(Name = "angles", EmitDefaultValue = true)]
        public List<double> Angles { get; set; }

        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            StringBuilder sb = new StringBuilder();
            sb.Append("class TextPosition {\n");
            sb.Append("  Origin: ").Append(Origin).Append("\n");
            sb.Append("  Angles: ").Append(Angles).Append("\n");
            sb.Append("}\n");
            return sb.ToString();
        }

        /// <summary>
        /// Returns the JSON string presentation of the object
        /// </summary>
        /// <returns>JSON string presentation of the object</returns>
        public virtual string ToJson()
        {
            return Newtonsoft.Json.JsonConvert.SerializeObject(this, Newtonsoft.Json.Formatting.Indented);
        }

        /// <summary>
        /// To validate all properties of the instance
        /// </summary>
        /// <param name="validationContext">Validation context</param>
        /// <returns>Validation Result</returns>
        IEnumerable<ValidationResult> IValidatableObject.Validate(ValidationContext validationContext)
        {
            yield break;
        }
    }

}