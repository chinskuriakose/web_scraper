# import requests
# from bs4 import BeautifulSoup
#
# url = 'https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-app.html'
# response = requests.get(url)
# soup = BeautifulSoup(response.content, 'html.parser')
#
# properties_section = soup.find("div", {"id": "cfn-amplify-app-properties"})
# print(properties_section)
# property_list = properties_section.find_all("div", {"class": "variablelist"})
#
# print(response)
# properties = {}
# for property_ in property_list:
#     key = property_.find("dt").text
#     value = property_.find("dd").text
#     properties[key] = value
#
# print(properties)

from bs4 import BeautifulSoup

html = '''<pre class="programlisting"><div class="cPtrdm-7KdwiPXSFFsHVgw== vJiSh2XhSD0llt9UwFq9AA==" data-testid="codeBtnContainer"><div class="btn-copy-code" title="Copy"><awsui-icon name="copy"></awsui-icon></div><button data-testid="copyCodeBtn" class="L0fhW8ft7887mExW5alCXw== awsui_button_vjswe_luxld_101 awsui_variant-normal_vjswe_luxld_126 awsui_button-no-text_vjswe_luxld_885" aria-label="Copy Type: AWS::ACMPCA::Certificate
Properties:
  ApiPassthrough:
    ApiPassthrough
  CertificateAuthorityArn: String
  CertificateSigningRequest: String
  SigningAlgorithm: String
  TemplateArn: String
  Validity:
    Validity
  ValidityNotBefore:
    Validity
" type="submit"><span class="awsui_icon_vjswe_luxld_905 awsui_icon-left_vjswe_luxld_905 awsui_icon_h11ix_1pphm_98 awsui_size-normal-mapped-height_h11ix_1pphm_151 awsui_size-normal_h11ix_1pphm_147 awsui_variant-normal_h11ix_1pphm_219"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" focusable="false" aria-hidden="true"><path class="stroke-linejoin-round" d="M2 5h9v9H2z"></path><path class="stroke-linejoin-round" d="M5 5V2h9v9h-3"></path></svg></span></button></div><code class="yaml hljs" tabindex="0"><span class="hljs-attr">Type:</span> <span class="hljs-string">AWS::ACMPCA::Certificate</span>
<span class="hljs-attr">Properties:</span>
  <a href="#cfn-acmpca-certificate-apipassthrough"><span class="hljs-attr">ApiPassthrough</span></a><span class="hljs-attr">:</span> <code class="replaceable">
    <a href="./aws-properties-acmpca-certificate-apipassthrough.html"><span>ApiPassthrough</span></a></code>
  <a href="#cfn-acmpca-certificate-certificateauthorityarn"><span class="hljs-attr">CertificateAuthorityArn</span></a><span class="hljs-attr">:</span> <code class="replaceable"><span>String</span></code>
  <a href="#cfn-acmpca-certificate-certificatesigningrequest"><span class="hljs-attr">CertificateSigningRequest</span></a><span class="hljs-attr">:</span> <code class="replaceable"><span>String</span></code>
  <a href="#cfn-acmpca-certificate-signingalgorithm"><span class="hljs-attr">SigningAlgorithm</span></a><span class="hljs-attr">:</span> <code class="replaceable"><span>String</span></code>
  <a href="#cfn-acmpca-certificate-templatearn"><span class="hljs-attr">TemplateArn</span></a><span class="hljs-attr">:</span> <code class="replaceable"><span>String</span></code>
  <a href="#cfn-acmpca-certificate-validity"><span class="hljs-attr">Validity</span></a><span class="hljs-attr">:</span> <code class="replaceable">
    <a href="./aws-properties-acmpca-certificate-validity.html"><span>Validity</span></a></code>
  <a href="#cfn-acmpca-certificate-validitynotbefore"><span class="hljs-attr">ValidityNotBefore</span></a><span class="hljs-attr">:</span> <code class="replaceable">
    <a href="./aws-properties-acmpca-certificate-validity.html"><span>Validity</span></a></code>
</code></pre>'''

soup = BeautifulSoup(html, 'html.parser')

# Extract the 'Type' value from the code block
type_element = soup.find('code', {'class': 'yaml'}).find('span', {'class': 'hljs-attr'}, text='Type:')
type_value = type_element.find_next_sibling('span').text.strip()

# Extract the properties as a dictionary
properties = {}
property_elements = soup.find_all('a', {'class': 'headerlink'})
print(property_elements)
for prop in property_elements:
    key = prop.text
    value = prop.find_next_sibling('code').text.strip()
    properties[key] = value

print(f'Type: {type_value}')
print('Properties:')
for key, value in properties.items():
    print(f'  {key}: {value}')